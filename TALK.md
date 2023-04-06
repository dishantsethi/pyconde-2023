### [Slide 1]
Hello everyone, my name is Dishant, and I've been using python since the very start of my career. This is my first talk at pycon, infact this my first time I’m talking in a room with more than couple hundred people in it. I'm excited to be here today to share with you some of the insights and experiences that I've gained in “Async Programming”

Over the years, I've had the opportunity to work on a variety of web development projects, ranging from small-scale applications to large, complex systems. Today, I look forward to sharing my knowledge and experience with you all and hope to inspire and educate fellow Python Developers. Thank you for having me, and let's get started!

### [Slide 2]
I’m going to start off with a question. How many of you heard developers say that async programming can makes your code fast? How many of you have already worked on scaling web applications and implemented async programming? If yes, I’m assuming you could have used one of the methods I’m going to discuss as we proceed with the presentation. 

So, what is async programming. It is a way of programming to leverage the power of concurrency or concurrent operations/tasks. For example, what if instead of waiting for an HTTP request to finish before continuing execution, we start the other operations that are waiting in the queue. 

Asynchronous programming allows for the execution of multiple tasks concurrently, without blocking the main thread of execution. This is particularly useful when dealing with I/O bound operations, such as network requests or file input/output, where the application needs to wait for a response from an external source.

Without asynchronous programming, such operations would typically be performed synchronously, that means the application would wait for each operation to complete before moving on to the next. This can lead to significant delays, particularly when dealing with large datasets or slow network connections.

### [Slide 3]
Now the question comes, how python can be used to achieve asynchronocity? In the talk we was going to discuss 4 ways to achieve this and by the end of this talk we will ask compare the results of each way of achieving asynchronocity. 

These ways are Multiprocessing, Multithreading, Asyncio and using celery & redis.

### [Slide 4]
Before moving into asynchronous code. I’ve this pre written code snippet which makes a GET call to ‘httpbin.org’ 50 times and prints uuid one after the other. As we can see that this synchronous code is taking around 1sec per request, which is around 1min to complete the task. This can turn out to be very costly for organisations running at very high scale.



### [Slide 5]
So the first way we are going to discuss is Multiprocessing which is by far the most obvious way. 
From the terminal, you can start your script multiple times and then all the scripts are going to run independently or at the same time. The operating system that's underneath will take care of sharing your CPU resources among all those instances. 


Alternately we can use the python’s multiprocessing library to achieve the same. It provides a Process class to create a new process, a Queue class to share data between processes, and other synchronization primitives such as Lock, Semaphore, and Event. In this example I’ve created a pool which is basically encapsulation of all the processes I want to run. And we can clearly see that the requests which took around 1 min earlier are taking around 10-12 seconds. That’s the power of asynchronous programming.

### [Slide 6]
But the question is, can we make is more fast? Obviously yes. The next way we are going to discuss is multithreading. Earlier we started multiple processes to execute one http call. But now we are going to start threads to do our job. 
A thread is a line of execution, pretty much like a process, but you can have multiple threads inside one process.

Again in this the OS takes care of sharing the CPU resources to multiple processes
Global Interpreter Lock (GIL) is a mechanism that ensures that only one thread executes Python bytecode at a time. This means that even if a Python program uses multiple threads, only one thread can execute Python code at any given time.
Although the GIL can limit the performance of multithreaded Python programs, it provides several benefits, including simplified memory management and a simplified programming model.

However, if you want to use multithreading in Python, you can still use it to perform I/O-bound tasks, such as network requests or file I/O, where the performance is limited by factors outside of the GIL.

Now if we try to run this code snippet, we can se that the same task of hitting http requests is done in 5-6 seconds.

### [Slide 7]
Another asynchronous technique we are going to look into is asyncio. This library just like multithreading does context switching to achieve concurrency but how it differs from multithreading is, it only uses a single thread per process and secondly, it is your code which decides when to leave control of a running thread so that some other portion of your code can run in the meantime. This is unlike multithreading, where this was done done by the library itself

Asyncio allows you to write code that can handle many I/O-bound operations concurrently, without blocking other parts of your program. This is achieved by using coroutines, which are functions that can be paused and resumed without blocking the event loop. Coroutines are defined using the async def syntax in Python.

Now whenever we create an async function using asyncio, we need to create an eventloop. This eventloop is responsible for handling the executions of all the corouteins or we can say our async functions. And in this particular example we will be using aiohttp because requests library is blocking or we can say synchronous in nature and await keyword can only be placed in front of coroutiens.

we can se that the same task of hitting http requests is done in 5-6 seconds.

### [Slide 8]
The last and the final way we are going to discuss for this session is Celery and Redis. Using asyncio and aiohttp may not always be in an option especially if you are using older versions of python. Also, there will be scenarios when you would want to distribute your tasks across different servers/threads/workers.

Celery is a task queue library that allows you to distribute tasks across multiple worker nodes. Celery uses a broker to handle communication between the client and the workers, and it supports multiple broker backends including Redis, RabbitMQ, and Amazon SQS.

Redis is an in-memory data store that can be used as a database, cache, and message broker. Redis is commonly used as a message broker with Celery because it provides a fast, reliable, and scalable way to pass messages between the client and the workers. We are also using redis as the backend to store results of celery tasks.
Here's an example of using Celery and Redis in a Python application, we how fast is this. Just 0.01 second to complete 50 api calls.

So, these are the ways in which we can achieve concurrency in python.
