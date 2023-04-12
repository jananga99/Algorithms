DONT USE PYTHON INFOINITE = float('inf)
USE 10**19 instead or the possible max value

You are given a disconnedted graph and you have to check whther there are negativ cycles init.

Of course, you can find connected componenets and apply bellamnd ford one by one but it is not the efficient and best wayt.

You can do this.

Here, dont check dist[u]==MAX before assigning values. Here we want to consider the disconnected ones as well. If there is a negative cycle even though these are unreachable therir values are still reducing at |V| iteration. So we can detect thos enegative cycles as well.