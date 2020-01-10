#!/usr/bin/env python3
import os
import json
import shutil
import sys
from ansible import context
from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C

class ResultCallback(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))
    def v2_runner_item_on_failed(self, result):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))

    def v2_runner_on_unreachable(self, result):
        host = result._host
        print(json.dumps({host.name: result._result}, indent=4))   

context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False,
                                connection='local',
                                diff = False,
                                forks=100,
                                start_at_task=None, 
                                extra_vars = (),
                                module_path=None,
                                check=False, become = None, become_method=None, become_user = None )

context.CLIARGS = ImmutableDict()

loader = DataLoader()
passwords = {}

results_callback = ResultCallback()
inventory = InventoryManager(loader=loader, sources=('/etc/ansible/hosts'))
variable_manager = VariableManager(loader=loader, inventory=inventory)

play_source =  dict(
    name = "Ansible Play",
    hosts = '127.0.0.1',
    gather_facts = 'no',
    tasks = [
        dict(action=dict(module='shell', args='ls /')),
        #dict(action=dict(module='shell', args='date'), register='shell_out2'),
        #dict(action=dict(module='debug', args=dict(msg='{{shell_out1.stdout}}')))
    ]
)


play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
tqm = None

try:
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords=passwords,
        stdout_callback=results_callback,
    )
    result = tqm.run(play)
    print(result)
except:
    e = sys.exc_info()[0]
    print( "Error: %s" % e )
finally:    
    if tqm is not None:
        tqm.cleanup()

    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)