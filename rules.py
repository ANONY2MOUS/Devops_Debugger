def detect_issue(log):
    log = log.lower()

    if "address already in use" in log:
        return {
            "problem": "Port already in use",
            "cause": "Another process is using the port",
            "fix": "Use lsof -i :<port> and kill the process"
        }

    elif "connection timed out" in log:
        return {
            "problem": "Network timeout",
            "cause": "Service unreachable",
            "fix": "Check server and firewall"
        }

    elif "cpu usage high" in log:
        return {
            "problem": "High CPU usage",
            "cause": "Process overload",
            "fix": "Use top or htop"
        }

    elif "no space left on device" in log:
        return {
            "problem": "Disk full",
            "cause": "Storage exhausted",
            "fix": "Clean disk space"
        }

    elif "service not running" in log:
        return {
            "problem": "Service down",
            "cause": "Service stopped",
            "fix": "Restart using systemctl"
        }

    return {
        "problem": "Unknown",
        "cause": "Not identified",
        "fix": "Check logs manually"
    }
