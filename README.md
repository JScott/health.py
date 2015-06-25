# Health check suite

Run `health.py` to collect data on server health.

Run `watch.py` to watch the data stream live.

Run `log.py` to stream that data to parsable file.

Each tool has a `--help` flag to find more info about the tool.

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
