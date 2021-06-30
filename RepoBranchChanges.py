from github import Github
include: "//a1lk_project_agilone_base/accesscontrol.lkml"



include: "//a1lk_project_agilone_base/accesscontrol.lkml"

import pandas as pd


branch_to_address='main'
##Csv File to read the repository Name from --Start

Url='https://docs.google.com/spreadsheets/d/1cHAjpigLd375XEw1B3Ohrn8Hsyagya2uStHHd_TGp1o/edit?usp=sharing'
repor= pd.read_csv("~/Downloads/RepoName.csv")

##Csv File to read the repository Name from --End


##Instance of Git Hub##--Start


git_instance = Github(login_or_token="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", base_url="https://api.github.com")
user = git_instance.get_user()
login = user.login
print('UserName: ' , user)


##Instanct of Git Hub## --End


##Iterate over the Repository from the csv 

for rindex,row in repor.iterrows():
    print('Repo Name running for....' , row[0])

    
    ## Repo Level Changes --Start

    
    repo = user.get_repo(row[0])
    repo.edit(allow_rebase_merge=False)
    repo.edit(allow_squash_merge=False)
    repo.edit(default_branch=branch_to_address)
    #repo.edit(fork = False)
    print('Repo Setting for allow rebase merge..... ',row[0],'  ' ,repo.allow_rebase_merge)
    print('Repo Setting for allow squash merge..... ',row[0],'  ' ,repo.allow_squash_merge)
    print('Repo Setting for default branch..... ',row[0],'  ' ,repo.default_branch)
    #print('Repo Setting for fork..... ',row[0],'  ' ,repo.fork)
    
  
    ## Repo Level Changes --End

    ##Branch Level Changes - Start

    
    branches = repo.get_branch(branch_to_address)
    print(branches)
    print(branches.protected)
    branches.edit_protection(enforce_admins=True, dismiss_stale_reviews=True, require_code_owner_reviews=True, required_approving_review_count=2)
    print(branches.protected)

    ##Branch Level Changes - end 

