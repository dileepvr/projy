# -*- coding: utf-8 -*-
""" Projy template for PythonPackage. """

# system
import subprocess
import sys
from datetime import date
# parent class
from projy.templates.ProjyTemplate import ProjyTemplate
# collectors
from projy.collectors.AuthorCollector import AuthorCollector
from projy.collectors.AuthorMailCollector import AuthorMailCollector


class OrgLaTeXOSATemplate(ProjyTemplate):
    """ Projy template class for PythonPackage. """

    def __init__(self):
        ProjyTemplate.__init__(self)

    def directories(self):
        """ Return the names of directories to be created. """
        directories_description = [
            self.project_name,
            self.project_name + '/styles',
        ]
        return directories_description

    def files(self):
        """ Return the names of files to be created. """
        files_description = [
            [self.project_name,
             '.gitignore',
             'OrgLaTeXGitignoreFileTemplate'],
            [self.project_name,
             'jabbrv-ltwa-all.ldf',
             'OrgLaTeXOSAJabbrv-ltwa-all-ldfFileTemplate'],
            [self.project_name,
             'jabbrv-ltwa-en.ldf',
             'OrgLaTeXOSAJabbrv-ltwa-en-ldfFileTemplate'],
            [self.project_name,
             'jabbrv.sty',
             'OrgLaTeXOSAJabbrv-styFileTemplate'],
            [self.project_name,
             'latexmkrc',
             'OrgLaTeXOSALatexmkrcFileTemplate'],
            [self.project_name,
             'osa-article.cls',
             'OrgLaTeXOSAOsa-article-clsFileTemplate'],
            [self.project_name,
             'osajnl.bst',
             'OrgLaTeXOSAOsajnl-bstFileTemplate'],
            [self.project_name,
             self.project_name + '.org',
             'OrgLaTeXOSAOsa-template-orgFileTemplate'],
            [self.project_name,
             self.project_name + '.bib',
             'OrgLaTeXOSASample-bibFileTemplate'],
            [self.project_name + '/styles',
             'aop.sty',
             'OrgLaTeXOSAStyles-aop-styFileTemplate'],
            [self.project_name + '/styles',
             'ao.sty',
             'OrgLaTeXOSAStyles-ao-styFileTemplate'],
            [self.project_name + '/styles',
             'boe.sty',
             'OrgLaTeXOSAStyles-boe-styFileTemplate'],
            [self.project_name + '/styles',
             'josaa.sty',
             'OrgLaTeXOSAStyles-josaa-styFileTemplate'],
            [self.project_name + '/styles',
             'josab.sty',
             'OrgLaTeXOSAStyles-josab-styFileTemplate'],
            [self.project_name + '/styles',
             'oe.sty',
             'OrgLaTeXOSAStyles-oe-styFileTemplate'],
            [self.project_name + '/styles',
             'ol.sty',
             'OrgLaTeXOSAStyles-ol-styFileTemplate'],
            [self.project_name + '/styles',
             'ome.sty',
             'OrgLaTeXOSAStyles-ome-styFileTemplate'],
            [self.project_name + '/styles',
             'optica.sty',
             'OrgLaTeXOSAStyles-optica-styFileTemplate'],
            [self.project_name + '/styles',
             'osac.sty',
             'OrgLaTeXOSAStyles-osac-styFileTemplate'],
            [self.project_name + '/styles',
             'osajournal.sty',
             'OrgLaTeXOSAStyles-osajournal-styFileTemplate'],
        ]
        return files_description

    def substitutes(self):
        """ Return the substitutions for the templating replacements. """
        author_collector = AuthorCollector()
        mail_collector = AuthorMailCollector()
        substitutes_dict = dict(
            project=self.project_name,
            project_lower=self.project_name.lower(),
            date=date.today().isoformat(),
            author=author_collector.collect(),
            author_email=mail_collector.collect(),
            virtual_env=sys.prefix.split('/')[-1],
        )
        return substitutes_dict

    def posthook(self):
        """ Posthook attempts to initialize and commit to git repository. """
        
        try:
            # pipe output to /dev/null for silence
            null = open("/dev/null", "w")
            subprocess.Popen("git", stdout=null, stderr=null)
            null.close()
            subprocess.call(["git", "init"])
            subprocess.call(["git", "config", "user.name", self.substitutes_dict['author']])
            subprocess.call(["git", "config", "user.email", self.substitutes_dict['author_email']])
            subprocess.call(["git", "add", "--all"])
            subprocess.call(["git", "commit", "-a", "-m", "'Initial template'"])

        except OSError:
            print("git not found")
        pass
