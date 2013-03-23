# -*- coding: utf-8 -*-
# Copyright (c) 2009-2012, Erkan Ozgur Yilmaz
# 
# This module is part of Stalker and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause

from stalker import db, User
from stalker.models.asset import Asset
from stalker.models.project import Project
from stalker.models.repository import Repository
from stalker.db.session import DBSession
from stalker.models.status import Status, StatusList
from stalker.models.task import Task
from stalker.models.type import Type

DBSession.remove()
DBSession.configure(extension=None)
db.setup()

status1 = Status(name="Complete", code="CMPLT")
status2 = Status(name="Pending Review", code="PRev")

repo1 = Repository(name="TestRepo")

project_status_list = StatusList(
    name="test",
    target_entity_type=Project,
    statuses=[status1]
)

project_type = Type(
    name="test",
    code='test',
    target_entity_type=Project
)

new_project1 = Project(
    name="test project1",
    code='tp1',
    type=project_type,
    status_list=project_status_list,
    repository=repo1
)

new_project2 = Project(
    name="test project2",
    code='tp2',
    type=project_type,
    status_list=project_status_list,
    repository=repo1
)

character_asset_type = Type(
    name="Character",
    code='char',
    target_entity_type=Asset
)

asset_status_list = StatusList(
    name="Asset Statuses",
    statuses=[status2],
    target_entity_type=Asset
)

new_asset1 = Asset(
    name="test asset",
    code='ta',
    type=character_asset_type,
    project=new_project1,
    status_list=asset_status_list
)

new_asset2 = Asset(
    name="test",
    code='t',
    type=character_asset_type,
    project=new_project2,
    status_list=asset_status_list
)

new_user1 = User(
    name="Test1",
    login="testuser1",
    email="testuser1@test.com",
    password="1234"
)

new_user2 = User(
    name="Test2",
    login="testuser2",
    email="testuser2@test.com",
    password="1234"
)

task_status_list = StatusList(
    name="Task Statuses",
    statuses=[status1, status2],
    target_entity_type=Task
)

new_task = Task(
    name="Task 1",
    resources=[new_user1],
    parent=new_asset1,
    status_list=task_status_list
)

new_task = Task(
    name="Task 2",
    resources=[new_user2],
    parent=new_asset2,
    status_list=task_status_list
)

#new_project.assets
#new_asset.project
#new_project
#new_project.assets.append(new_asset)
#new_project.assets

DBSession.add_all([new_project1, new_project2])
DBSession.commit()

# uses are now assigned to projects
assert new_project1.users == []
