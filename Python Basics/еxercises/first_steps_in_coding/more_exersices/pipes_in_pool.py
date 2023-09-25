pool_volume = int(input())
first_pipe = int(input())
second_pipe = int(input())
hours_absense = float(input())

first_pipe_fill = first_pipe * hours_absense
second_pipe_fill = second_pipe * hours_absense
pool_fill = first_pipe_fill + second_pipe_fill

pool_percent_fill = (pool_fill / pool_volume) * 100
first_pipe_percent_fill = (first_pipe_fill / pool_fill) * 100
second_pipe_percent_fill = (second_pipe_fill / pool_fill) * 100
overflow = 0
if pool_fill <= pool_volume:
    print(f'The pool is {pool_percent_fill:.2f}% full. Pipe 1: {first_pipe_percent_fill:.2f}%. Pipe 2: {second_pipe_percent_fill:.2f}%.')
elif pool_fill > pool_volume:
    overflow = pool_fill - pool_volume
    print(f'For {hours_absense:.2f} hours the pool overflows with {overflow:.2f} liters.')