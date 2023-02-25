Back to [All Modules](https://github.com/pyrustic/threadom/blob/master/docs/modules/README.md#readme)

# Module Overview

**threadom**
 
No description

> **Classes:** &nbsp; [Error](https://github.com/pyrustic/threadom/blob/master/docs/modules/content/threadom/content/classes/Error.md#class-error) &nbsp;&nbsp; [QueueTail](https://github.com/pyrustic/threadom/blob/master/docs/modules/content/threadom/content/classes/QueueTail.md#class-queuetail) &nbsp;&nbsp; [Threadom](https://github.com/pyrustic/threadom/blob/master/docs/modules/content/threadom/content/classes/Threadom.md#class-threadom)
>
> **Functions:** &nbsp; None
>
> **Constants:** &nbsp; None

# Class Threadom
No description.

## Base Classes
object

## Class Attributes
No class attributes.

## Class Properties


# All Methods
[\_\_init\_\_](#__init__) &nbsp;&nbsp; [consume](#consume) &nbsp;&nbsp; [info](#info) &nbsp;&nbsp; [pause](#pause) &nbsp;&nbsp; [q](#q) &nbsp;&nbsp; [resume](#resume) &nbsp;&nbsp; [run](#run) &nbsp;&nbsp; [stop](#stop) &nbsp;&nbsp; [\_consume](#_consume) &nbsp;&nbsp; [\_dispatch\_exception](#_dispatch_exception) &nbsp;&nbsp; [\_dispatch\_result](#_dispatch_result) &nbsp;&nbsp; [\_is\_valid\_qid](#_is_valid_qid) &nbsp;&nbsp; [\_loop](#_loop) &nbsp;&nbsp; [\_run](#_run) &nbsp;&nbsp; [\_run\_consumer](#_run_consumer) &nbsp;&nbsp; [\_run\_next\_synced\_target](#_run_next_synced_target) &nbsp;&nbsp; [\_runner](#_runner) &nbsp;&nbsp; [\_short\_loop](#_short_loop)

## \_\_init\_\_
- tk: a tk.Tk instance or any tkinter object
- sync: boolean



**Signature:** (self, tk, sync=False)





**Return Value:** None

[Back to Top](#module-overview)


## consume
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



**Signature:** (self, queue, consumer=None, unpack\_result=False, exception\_handler=None, latency=10)





**Return Value:** None

[Back to Top](#module-overview)


## info
Retrieve info from the process launched by the method 'consume'.
Returns a dict:
 {"queue": queue, "active": boolean, "consumer": callback, "unpack_result": boolean,
 "exception_handler": callback, "latency": integer}



**Signature:** (self, qid=None)





**Return Value:** None

[Back to Top](#module-overview)


## pause
Pause the process launched by the method 'consume'.
Put 0 to pause all processes



**Signature:** (self, qid)





**Return Value:** None

[Back to Top](#module-overview)


## q
Creates a new Queue.
Usage:
    queue.put(data)



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## resume
Resume the process launched by the method 'consume'
Put 0 to resume all processes



**Signature:** (self, qid)





**Return Value:** None

[Back to Top](#module-overview)


## run
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



**Signature:** (self, target, target\_args=None, target\_kwargs=None, consumer=None, sync=None, daemon=True, unpack\_result=False, upstream\_exception\_handler=None, downstream\_exception\_handler=None)





**Return Value:** None

[Back to Top](#module-overview)


## stop
Stop the process launched by the method 'consume'.
Set 0 to stop them all.



**Signature:** (self, qid)





**Return Value:** None

[Back to Top](#module-overview)


## \_consume
No description



**Signature:** (self, queue, consumer, unpack\_result, exception\_handler, latency)





**Return Value:** None

[Back to Top](#module-overview)


## \_dispatch\_exception
No description



**Signature:** (self, exception, exception\_handler)





**Return Value:** None

[Back to Top](#module-overview)


## \_dispatch\_result
No description



**Signature:** (self, result, consumer, unpack\_result, exception\_handler)





**Return Value:** None

[Back to Top](#module-overview)


## \_is\_valid\_qid
No description



**Signature:** (self, qid)





**Return Value:** None

[Back to Top](#module-overview)


## \_loop
No description



**Signature:** (self, qid)





**Return Value:** None

[Back to Top](#module-overview)


## \_run
No description



**Signature:** (self, target, target\_args, target\_kwargs, consumer, sync, daemon, unpack\_result, upstream\_exception\_handler, downstream\_exception\_handler)





**Return Value:** None

[Back to Top](#module-overview)


## \_run\_consumer
No description



**Signature:** (self, consumer, result, unpack\_result)





**Return Value:** None

[Back to Top](#module-overview)


## \_run\_next\_synced\_target
No description



**Signature:** (self)





**Return Value:** None

[Back to Top](#module-overview)


## \_runner
No description



**Signature:** (self, queue, target, target\_args, target\_kwargs, exception\_handler)





**Return Value:** None

[Back to Top](#module-overview)


## \_short\_loop
No description



**Signature:** (self, queue, consumer, unpack\_result, upstream\_exception\_handler, downstream\_exception\_handler)





**Return Value:** None

[Back to Top](#module-overview)



