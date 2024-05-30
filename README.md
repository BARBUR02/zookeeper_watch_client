### Simple zookeper Watch app

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
