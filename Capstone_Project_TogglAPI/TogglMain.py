
"""
    Summary: Toggl API to fetch information about the Toggl workspace, Clients, and Projects in Toggl.
    In this version reports are displayed on-screen and written to a csv file.

    In addition, users can update the default hourly rate, and apply the new default
    hourly rate to all projects if they choose to. Examples of changing specific project hourly
    rates are provided as well.

    All workspace, client, and project information is stored in a single TogglWorkspace object.
    Only the primary (company) workspace is checked. Personal workspaces are not.

    In the future, this will be part of a web application for simple project management.

    Note: This is based on the free version of Toggl. For more information about Toggl, see
    https://www.toggl.com

    Required: To create a Toggl Workspace object, the user must provide a valid Toggl API token. Some features require
              the user to be an admin.

    Exceptions: API invalid, errors in creating TogglWorkspace object, updating default_hourly_rates,
                project rates, estimated project hours, errors printing reports to the screen and errors creating
                csv file reports.

    :return: None
"""
import sys
from TogglWorkSpace import TogglWorkSpace


def main():
    """
    Main prompts the user for his or her Toggl API, checks for validity, and creates the
    TogglWorkspace object. Select Workspace information is displayed on-screen.

    Main then asks if the user wants to change the default hourly rate. If the response is yes,
    the user is prompted to enter the new rate. This is followed by a prompt to update all project
    rates to the new default hourly rate. This follows with an attempt to print the summary report.

    This is followed by examples of changing specific project hourly rates, passing either the
    project ID or project name, as well as updating the estimated hours for a specific project.
    Another project summary report is displayed on-screen to confirm the changes.

    Finally, a series of reports is printed (Workspace Report, Client Report, Projects Report, and
    a Summary Report.

    Variables:
                my_api_token: str - user's Toggl API token
                my_workspace: ToggleWorkSpace object - contains workspace, project, and client information
                new_rate: int - default rate for workspace
                answer: str - yes/no response to updating default hourly rate and update all projects with default rate


    Exceptions:
                If the user doesn't answer the prompts with expected input, an error message displays.
                If the project summary report can't be displayed, an error message occurs.
    :return: None
    """

    # Get the Toggl API token and check for validity
    my_api_token = str(input("Please enter your Toggl API token from https://www.toggl.com/app/profile: "))

    try:
        my_workspace = TogglWorkSpace(my_api_token)
    except Exception:
        print("Invalid API token. Exiting program now.")
        sys.exit()
    else:
        # Display the __workspace info for the Toggl Workspace object
        my_workspace.print_workspace_info()

        # Prompt user to change the default hourly rate
        answer = input("\nWould you like to change the default hourly rate?  ").lower().strip()
        if answer == 'y' or answer == 'yes':
            try:
                new_rate = int(input("\n\nEnter the new default hourly rate as a whole number:  ".strip()))
                my_workspace.set_default_hourly_rate(new_rate)

            except Exception:
                print("Invalid value for default hourly rate.")
        else:
            print("No changes will be made to default hourly rate.")

        # Prompt user to update project rate to the new default hourly rate
        answer = input("\nUpdate all projects to the default hourly rate?  ").lower().strip()
        if answer == 'y' or answer == 'yes':
            try:
                my_workspace.update_projects_rate()
            except Exception:
                print("Unable to update hourly rate for all projects.")
        else:
            print("No changes made to project hourly rates.")

        # Print project summary report
        try:
            my_workspace.print_summary_report()
        except Exception:
            print("Unknown Error. Unable to retrieve project summary report.")

        # Update hourly rate by project ID and project name
        try:
            my_workspace.set_project_hourly_rate(50,'15726464', 'id')
            my_workspace.set_project_hourly_rate(75, 'Cranium 360 Portal', 'name')
            my_workspace.set_project_hourly_rate(95, '15726460', 'id')

            # Update estimated hours by project id
            my_workspace.set_project_estimated_hours(650, '15726460', 'id')

        except Exception:
            print("Error updating hours. Please ensure project exists, project name, id, and hours are correct.")

        # Reprint the summary report to show all changes
        try:
            my_workspace.print_summary_report()
        except Exception:
            print("Unknown Error. Unable to retrieve project summary report.")

        # Write reports for workspace info, client info, project info, and a summary report
        try:
            my_workspace.workspace_report()
            my_workspace.client_report()
            my_workspace.projects_report()
            my_workspace.summary_report()
        except Exception:
            print("Unknown Error. Could not print one or more reports.")

main()