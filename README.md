# Health check suite

Run `health.py` to collect data on server health.

Run `watch.py` to watch the data stream live.

Run `log.py` to stream that data to parsable file.

Each tool has a `--help` flag to find more info about the tool.

## Architecture

The `health.py` daemon is responsible for collecting and storing data in a central place.

All other executables grab from this and do what they will with the data. This way we can extend the data to whatever is most helpful to our sysadmin. The provided example is file and terminal output, which is barely helpful to her, but it would take minutes to write something that would be more appopriate at the moment.

Between `shelve` and `system('clear')`, I doubt much of this will work on windows. Sorry.

## TODO

- TESTS. I feel dirty.
- Break things into modules
- Have a centralized module deal with derived data
- PID and log files for the processes
- More useful output:
    - IRC
    - Slack
- More derived data:
    - Recovery time
    - Response time statistics
- Replace all this file DB stuff with ZMQ messaging
