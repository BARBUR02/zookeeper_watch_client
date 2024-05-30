### Simple zookeper Watch app
## Description
App programmatically watches for changes on specified zookeeper node. 
Apart from python application, there is also provided set of utility commands
to interact with zookeeper environment in replicated mode. Whole zookeeper specific
part is dockerized. For interaction with zookeeper from python client I am utilizing `kazoo`.


## Zookeper setup
If you have `Taskfile` installed, run `task -l` to see supported commands.
If you don't, just check out `Taskfile.yml` and copy appropriate commands.

#### To start zookeper servers in replicated mode (docker-compose created 3 instances) run:
```sh
task start_servers_in_replicated_mode
```
#### To start dedicated zookeper server (in replicated mode) run:
```sh
task start_servers_in_replicated_mode
```
#### To connect to specific zookeper instance from command line, run:
```sh
task command_line_client SERVER={server_name}
```

#### To run an actual app, execute `task run_watcher`
Remember to change `node_name` and `application_path` parameters, in my case it's MacOS application specific path:
```sh
task command_line_client SERVER={server_name}
```
