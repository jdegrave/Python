import requests
import sys
from requests.auth import HTTPBasicAuth
import csv
# import base64  - for future
# from datetime import datetime - for future

class TogglWorkSpace:
    """
    TogglWorkSpace is a class that contains Toggl workspace information, client information, and project information for
    a specific instance of a Toggl workspace. Its purpose is to fetch, manipulate, and extend information available
    from various Toggl APIs.

    Toggl APIs:  Toggl APIs have a one or two base URL formats. All response are returned in json format.


    TogglWorkspace Constants:

    BASE_TOGGLE_API_URL - str - the base Toggle API URL from which workspace, client and project URL APIs are built
    WORKSPACES_URL - str - initially set to an empty string, will contain the BASE_TOGGLE_API_URL and other info
    HEADERS - dict - indicates the content type is json (JavaScript Object Notation)
    WORKSPACE_PARAMS - dict - initially set to only active projects and actual hours.


    ToggleWorkspace Class Variables:

    self.__my_api_token - str - user-provided Toggl API token
    self.__workspace - dict - all workspace key: value pairs returned from workspaces API
    self.__workspace_projects - list of dicts - all project key: value pairs for each project from project API
    self.__clients - list of dicts - all client key: value pairs for client from client API
    self.__wid - int - unique identifier that is the "Workspace ID" returned from workspace API
    self.__project_count - int - total number of projects in the workspace


    TogglWorkspace Functions:

    __init__(api_token): Builds the basic workspace, client, and project API URLs using Toggl API token, initialization.

    get_workspace_info:  Builds the workspace API URL and returns a dictionary of the workspace info
    get_workspace_id:  Returns str - the workspace id
    get_workspace_name: Returns str - the name of the workspace
    get_is_admin: Returns bool - True if the api is for a Toggl admin for the workspace, false otherwise
    get_default_hourly_rate: Returns int -  For free version of Toggl, this is always zero and can't be set within Toggl
    get_default_currency: Returns str - the default currency ('USD' = United States dollar)
    get_workspace_projects: Fetches list of dicts - Builds projects API URL and fetches project info
    get_client_list: Fetches list of dicts - Builds clients API URL and fetches client info
    get_project_count: Returns int of total number of projects in the workspace

    set_default_hourly_rate: Returns None - sets the workspace's billable rate
    update_projects_rate: Returns None - updates all projects to the default hourly rate
    set_project_hourly_rate: Returns None - sets the specific project's billable rate; parameters are project ID or name
    set_project_estimated_hours: Returns None - sets estimated project duration (hrs) for a specific project

    print_workspace_info: Returns None - displays some of the workspaces values on-screen
    print_summary_report: Returns None - displays a combination of workspace, client, and project values on-screen

    workspace_report: Returns None - creates a csv file of a limited number of workspace attributes (values)
    projects_report: Returns None - creates a csv file of a limited number of project attributes (values)
    client_report: Returns None - creates a csv file of a limited number of client attributes (values)
    summary_report: Returns None - creates a csv file of specific workspace, project, and client attributes(values)


    TogglWorkspace Exceptions:

    Exceptions created for invalid API token, inability to get or create workspace dictionary, client list, and
    project list. In addition, getters for workspace name, id, default_hourly_rate, is_admin, and default_currency also
    have exceptions


    """

    BASE_TOGGL_API_URL = 'https://www.toggl.com/api/v8/workspaces'
    WORKSPACES_URL = ''
    HEADERS = {'content-type': 'application/json'}
    WORKSPACE_PARAMS = {'active': 'true','actual_hours': 'true'}

    def __init__(self, my_api_token):
        """
        Constructor for TogglWorkSpace object. Initializes TogglWorkSpace properties. Calls the get_workspace_info()
        function first. Everything is driven off the workspace ID ("wid"). All workspace, client, and project informa-
        tion available in Toggl is fetched. Toggl returns different information based on plan pricing.

        Variables:

        self.__my_api_token - str - user-provided Toggl API token
        self.__workspace - dict - all workspace key: value pairs returned from workspaces API
        self.__workspace_projects - list of dicts - all project key: value pairs for each project from project API
        self.__clients - list of dicts - all client key: value pairs for client from client API
        self.__wid - int - unique identifier that is the "Workspace ID" returned from workspace API
        self.__project_count - int - total number of projects in the workspace


        Exceptions:  Invalid API token, failure to retrieve workspace, client, and/or project details from Toggle API
                     If it can't fetch the workspace, client and project info from Toggl, program terminates.

        :param my_api_token: str - required
        :return: TogglWorkSpace object
        """

        self.__my_api_token = my_api_token

        if self.__my_api_token == '':
            print('No API token provided. Quitting program now.')
            sys.exit()

        self.__workspace = {}
        self.__workspace_projects = {}
        self.__clients = {}
        self.__wid = -1
        self.__project_count = 0

        try:
            self.__get_workspace_info()

            if self.__wid == -1:
                print('Please create a Toggl Workspace object. Project details can not be retrieved without a '
                      'valid Workspace ID (wid). Exiting Program now')
                sys.exit()

            else:
                self.WORKSPACES_URL = self.BASE_TOGGL_API_URL + '/' + str(self.__wid)
                self.__get_workspace_projects()
                self.__get_client_list()

        except Exception:
            print('Cannot get workspace data, project data, and/or client data. '
                  'Check to ensure API token and API URL are correct.')
            sys.exit()

    def __get_workspace_info(self):
        """
        Private function to fetch info form a single workspace info from Toggl. Toggle returns a list of dictionaries.
        Because the TogglWorkSpace class only works with one workspace (the primary or company workspace), the list
        is transformed into just a dictionary to make processing easier.

        The wid ("Workspace ID") is extracted into its own variable.

        Exceptions: Connection Error, HTTP error, Timeout, RequestsException, and general Exception
        :return: None
        """
        try:
            all_workspaces = requests.get(self.BASE_TOGGL_API_URL, headers=self.HEADERS,
                                          auth=HTTPBasicAuth(self.__my_api_token, 'api_token'))
        except ConnectionError:
            print('Connection issue. Please check your internet connection.')
        except requests.HTTPError:
            print('HTTP Error')
        except requests.Timeout:
            print('Timeout error. Try again later.')
        except requests.RequestException:
            print('API token is not valid.')
        except:
            print('API token not valid.')
        else:
            self.__workspace = all_workspaces.json()
            self.__workspace = self.__workspace[0]
            self.__wid = self.get_workspace_id()

    def get_workspace_id(self):
        """
        Function to get workspace id.
        Exceptions: Failed attempt to retrieve workspace ID from workspace dictionary
        :return: self.__wid - str
        """
        try:
            self.__wid = self.__workspace['id']
            return self.__wid
        except Exception:
            print('Error. Could not retrieve Workspace ID. Check API token and try again.')

    def get_workspace_name(self):
        """
        Function to return workspace name.
        Exceptions: Failed attempt to retrieve workspace name from workspace dictionary
        :return: workspace name - str
        """

        try:
            return self.__workspace['name']
        except Exception:
            print('Error. Could not retrieve Workspace name. Ensure API token is valid.')

    def get_is_admin(self):
        """
        Function to return if the API token passed was for a Toggl admin or not.
        Exceptions: Failed attempt to retrieve admin status from workspace dictionary.
        :return: workspace admin - bool
        """
        try:
            return self.__workspace['admin']
        except Exception:
            print('Error. Could not retrieve Workspace Admin information. Ensure API token is valid.')

    def get_default_currency(self):
        """
        Function to return the default currency
        Exceptions: Failed attempt to retrieve default currency from workspace dictionary.
        :return: default currency - str
        """
        try:
            return self.__workspace['default_currency']
        except Exception:
            print('Error. Could not retrieve default_currency information. Ensure API token is valid.')

    def get_default_hourly_rate(self):
        """
        Function to return the default hourly rate from the workspace dictionary. Default currency applies to all
        projects and clients. The free version of Toggl does not allow setting of the default hourly rate from within
        Toggl; therefore, the default value is always zero ("0").

        Exceptions: Failed attempt to retrieve the default hourly rate from the workspace dictionary.
        :return: default hourly rate - int
        """

        try:
            return self.__workspace['default_hourly_rate']
        except Exception:
            print('Error. Could not retrieve default hourly rate information. Ensure API token is valid')

    def __get_workspace_projects(self):
        """
        Function to call the Toggl projects API to get project information for all projects in the workspace. It also
        sets all projects "billable" key to "True", and adds a key:value pair for estimated hours for each project.
        Estimated hours value is set to zero as the default, and each project's rate is set to the default hourly rate.
        Finally, the total number of active projects is counted.
        Exceptions: None
        :return: None
        """

        WORKSPACE_PROJECTS_URL = self.WORKSPACES_URL + '/projects'
        all_workspace_projects = requests.get(WORKSPACE_PROJECTS_URL, json=self.WORKSPACE_PARAMS, headers=self.HEADERS,
                                              auth=HTTPBasicAuth(self.__my_api_token, 'api_token'))
        self.__workspace_projects = all_workspace_projects.json()

        for project in self.__workspace_projects:
            project['billable'] = True
            project['estimated_hours'] = 0
            project['rate'] = self.get_default_hourly_rate()
            self.__project_count += 1

    def __get_client_list(self):
        """
        Function to fetch the client information from the Toggl API. It builds the API URL for clients, and then
        puts the json response into a list of dictionaries.
        Exceptions: None
        :return: None
        """
        CLIENT_LIST_URL = self.WORKSPACES_URL + '/clients'
        all_workspace_clients = requests.get(CLIENT_LIST_URL, json=self.WORKSPACE_PARAMS, headers=self.HEADERS,
                                             auth=HTTPBasicAuth(self.__my_api_token, 'api_token'))
        self.__clients = all_workspace_clients.json()

    def set_default_hourly_rate(self, rate):
        """
        Function to set the default hourly rate in the workspace dictionary. Normally this function would be called
        after the TogglWorkSpace object is instantiated, since when created, free Toggl accounts set this value to zero.
        :param rate: int - default hourly rate
        Exceptions: None
        :return: None
        """
        try:
            self.__workspace['default_hourly_rate'] = rate
        except Exception:
            print("Please enter the hourly rate as an integer.")
        else:
            print("Default hourly rate is now: ", self.__workspace['default_hourly_rate'])

    def update_projects_rate(self):
        """
        Function to set all projects in the projects list to the default hourly rate stored in the workspaces
        dictionary. Normally, update_projects_rate() function would be called after calling the
        set_default_hourly_rate() function.
        Exceptions: None
        :return: None
        """
        for project in self.__workspace_projects:
            project['rate'] = self.__workspace['default_hourly_rate']
        print("All projects updated to reflect default hourly rate.")

    def set_project_hourly_rate(self, h_rate, key, key_type):
        """
        Function to set the hourly rate for a specific project. The parameters are the rate, the value
        of the associated key type, and the key for the project to update. This function expects key_type to be either
        the project id ('id') or the project name ('name') from the self.__workspace_projects list.

        :param h_rate: int - new hourly rate for the project
        :param key: int or str - value of the key type parameter
        :param key_type: int or str - values are 'id' or 'name'
        Exceptions: None
        :return: None
        """

        for project in self.__workspace_projects:
            current_key = str(project.get(key_type))

            if current_key == key:
                project['rate'] = h_rate
                print("\nThe hourly rate for Project", project['name'], "has been updated to", project['rate'],
                      self.__workspace['default_currency'])
                break

    def set_project_estimated_hours(self, estimate, key, key_type):
        """
        Function to set the estimated hours for a specific project. The parameters are the hours estimated, the value
        of the associated key type, and the key for the project to change. This function expects key_type to be either
        the project id ('id') or the project name ('name') from the self.__workspace_projects list.
        :param estimate: int - number of hours needed to complete project
        :param key: int or str - value of the key type parameter
        :param key_type: int or str - values are 'id' or 'name'
        Exceptions: None
        :return: None
        """

        for project in self.__workspace_projects:
            current_key = str(project.get(key_type))

            if current_key == key:
                project['estimated_hours'] = estimate
                print("\nThe estimated hours for Project", project['name'], "has been updated to",
                      project['estimated_hours'], "hours.")
                break

    def get_project_count(self):
        """
        Function to return the total number of active projects in the workspace from the project list.
        Exceptions: None
        :return: self.__project_count - str
        """
        return self.__project_count

    def print_workspace_info(self):
        print("\nTOGGL WORKSPACE DESCRIPTION")
        print(format("Workspace Name: ", "<25s"), format(self.get_workspace_name(),">15s"))
        print(format("Workspace ID ('wid'): ", "<25s"), format(str(self.get_workspace_id()), ">15s"))
        print(format("Default Hourly Rate: ", "<25s"), format(str(self.get_default_hourly_rate()), ">15s"),
              self.get_default_currency())
        print(format("Count of Total Active Projects: ", "<25s"), format(str(self.get_project_count()), ">8s"))
        print()

    def print_summary_report(self):
        """
        Function to display specific project information on-screen. Combines information from the workspace dictionary,
        projects list and clients list into one summary report. This summary has slightly less information than the
        summary csv file created from summary_report() function
        Exceptions: None
        :return: None
        """

        # Print the header
        print('\nPROJECT SUMMARY\n')
        print(format('Client ID', "<11s"),
              format('Client Name',"<26s"),
              format('Project ID', "<12s"),
              format('Project Name',"<30s"),
              format('Billable', "<10s"),
              format('Actual Hours',">15s" ),
              format('Rate',">7s"),
              format('Total Earnings',">20s"),
              format('Estimated Hours', ">20s"))

        # Get the workspace, project, and client information and print to the screen.
        for project in self.__workspace_projects:
            print(format(project['cid'],"<9d"), end='\t')

            # Get the client name
            for client in self.__clients:
                if str(client['id']) == str(project['cid']):
                    print(format(client['name'],"<25s"), end='\t')
                    break

            print(format(project['id'], "<9d"),end='\t')
            print(format(project['name'], "30s"), end='\t')
            print(format(str(project['billable']), ">5s"), end='\t\t')
            print(format(project['actual_hours'], ">8"), end='\t\t')
            print(format(project['rate'], ">4" ),end='\t\t')
            print(format(project['actual_hours'] * project['rate'], ">8d"), self.__workspace['default_currency'], end='\t')
            print(format(project['estimated_hours'], ">14"))

    def workspace_report(self):
        """
        Function to create a csv file with headers for limited workspace information:
        - name, workspace ID, default hourly rate, default currency, billable status
        Exceptions: None
        :return: None
        """
        with open('workspace_report', 'wt') as ws_report:
            field_names = ['name', 'id', 'default_hourly_rate', 'default_currency', 'projects_billable_by_default',]
            report_object = csv.DictWriter(ws_report, fieldnames=field_names, restval='', extrasaction='ignore',
                                           lineterminator='\n')
            report_object.writeheader()
            report_object.writerow(self.__workspace)

    def client_report(self):
        """
        Function to create a csv file with headers for limited client information:
        - client ID, client name
        Exceptions: None
        :return: None
        """
        with open('client_report', 'wt') as cl_report:
            field_names = ['id', 'name']
            report_object = csv.DictWriter(cl_report, fieldnames=field_names, restval='', extrasaction='ignore',
                                           lineterminator='\n')
            report_object.writeheader()
            for client in self.__clients:
                report_object.writerow(client)

    def projects_report(self):
        """
        Function to create a csv file with headers for limited project information:
        - client id, project id, project name, actual hours, estimated hours, billable status, active status, and total
        active projects
        Exceptions: None
        :return: None
        """
        with open('projects_report', 'wt') as pr_report:
            field_names = ['cid','id', 'name', 'actual_hours', 'estimated_hours', 'billable', 'active',]
            report_object = csv.DictWriter(pr_report, fieldnames=field_names, restval='', extrasaction='ignore',
                                           lineterminator='\n')
            report_object.writeheader()
            for project in self.__workspace_projects:
                report_object.writerow(project)

            report_object = csv.writer(pr_report)
            report_object.writerow(['Total Active Projects', str(self.get_project_count())])

    def summary_report(self):
        """
        Function to create a csv file with summary information from the Toggl workspace, projects, and clients, with
        headers. Information is gathered from each variable (workspace dict, projects list, and client list) and
        combined into this report.
        Exceptions: None
        :return: None
        """
        with open('summary_report', 'wt') as sum_report:
            sum_header = ['WID', 'Workspace Name', 'Client ID', 'Client Name', 'Project ID', 'Project Name',
                          'Actual Hours', 'Estimated Hours', 'Billable', 'Active']
            report_object = csv.writer(sum_report, dialect='excel', lineterminator='\n')
            report_object.writerow(sum_header)

            # Get workspace info
            ws_list = [self.get_workspace_id()]
            ws_list.append(self.get_workspace_name())

            # Get project info for all projects
            for project in self.__workspace_projects:
                pr_list = []
                pr_list.append(project['cid'])

                # Get client name associated with the project
                for client in self.__clients:
                    if client['id'] == project['cid']:
                        pr_list.append(client['name'])
                        break

                pr_list.append(project['id'])
                pr_list.append(project['name'])
                pr_list.append(project['actual_hours'])
                pr_list.append(project['estimated_hours'])
                pr_list.append(project['billable'])
                pr_list.append(project['active'])

                # Combine the workspace list with the project list
                row = ws_list + pr_list

                # write the data row for each project
                report_object.writerow(row)
