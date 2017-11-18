# pipes live in kernel mem
# efficient, big block of mem inside kernel and managed by kernel
# pipes are fixed size
# pipe will block on write if no more room in pipe (can cause deadlocks...)
# O_NONBLOCK - to not block on writes to full pipe, you can re-try after doing something...
