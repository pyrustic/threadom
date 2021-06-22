
Back to [Reference Overview](https://github.com/pyrustic/threadom/blob/master/docs/reference/README.md)

# threadom.\_\_init\_\_



<br>


```python

class Error:
    """
    Common base class for all non-exit exceptions.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

```

<br>

```python

class QueueTail:
    """
    Use this class as an indicator of the tail of a queue 
    """

```

<br>

```python

class Threadom:
    """
    
    """

    def __init__(self, tk, sync=False):
        """
        - tk: a tk.Tk instance or any tkinter object
        - sync: boolean
        """

    def consume(self, queue, consumer=None, unpack_result=False, exception_handler=None, latency=10):
        """
        Loops through the queue, pick data, then run the callback 'consumer' with
        data as argument.
        Example, assume that there are these integers 3, 4 and 5 in the queue.
        3 -> consumer(3); 4 -> consumer(4); 5 -> consumer(5)
        
        - queue: the queue. See Threadom's method 'q'.
        - consumer: the callback that accepts one argument or more than one if unpack_result is True
        - unpack_result: if True, the result will be unpacked.
        - exception_handler: callback that accepts one argument to handle any occurred exception.
        - latency: integer. Milliseconds between each loop to consume the queue. By default: 10
        
        Returns the 'qid'. You will need this 'qid' to stop, pause, resume the loop or to get info.
        """

    def info(self, qid=None):
        """
        Retrieve info from the process launched by the method 'consume'.
        Returns a dict:
         {"queue": queue, "active": boolean, "consumer": callback, "unpack_result": boolean,
         "exception_handler": callback, "latency": integer}
        """

    def pause(self, qid):
        """
        Pause the process launched by the method 'consume'.
        Put 0 to pause all processes
        """

    def q(self):
        """
        Creates a new Queue.
        Usage:
            queue.put(data)
        """

    def resume(self, qid):
        """
        Resume the process launched by the method 'consume'
        Put 0 to resume all processes
        """

    def run(self, target, target_args=None, target_kwargs=None, consumer=None, sync=None, daemon=True, unpack_result=False, upstream_exception_handler=None, downstream_exception_handler=None):
        """
        Runs a target in background. Return False if the target is in WAITING state (sync)
        - target: the callable to run
        - target_args: tuple, arguments to use
        - target_kwargs: dict, keyword-arguments to use
        - consumer: the callback with parameter(s) that will consume the returned value by target
        - sync: None or boolean to override the constructor's argument sync
        - unpack_result: boolean, True, to unpack the result returned by target
        - upstream_exception_handler: one parameter callback to handle the exception
            raised while running the target
        - downstream_exception_handler: one parameter callback to handle the exception
            raised while calling the consumer
        """

    def stop(self, qid):
        """
        Stop the process launched by the method 'consume'.
        Set 0 to stop them all.
        """

```

