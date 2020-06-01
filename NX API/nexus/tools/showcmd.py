def get_command(cmd):
    showcmd = {
      "ins_api": {
        "version": "1.0",
        "type": "cli_show",
        "chunk": "0",
        "sid": "1",
        "input": cmd,
        "output_format": "json"
      }
    }

    return showcmd