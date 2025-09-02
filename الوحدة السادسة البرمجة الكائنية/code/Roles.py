class ProgrammerRole:
    def __init__(self, lang, projects=None):
        self.lang = lang
        if projects is None:
            projects = []
        self.projects = projects

    def assign_project(self, project):
        self.projects.append(project)

    def get_projects(self):
        print("Projects:")
        print('=' * 10)
        project_list = []
        for number, project in enumerate(self.projects):
            project_list.append(f'{number + 1}. {project}')
        return '\n'.join(project_list)