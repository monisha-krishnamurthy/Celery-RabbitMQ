from celery import Celery       #import celery function from celery package

app = Celery()   #backend- optional parameter to query the status of a background task/retrieve its results

#build celery tasks


@app.task(ignore_result=True) #Each celery task must be introduced with the decorator @app.task. This allows celery to identify functions that it can add its queuing functions to
def print_hello():
    print('hello there')

@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in range(i*i, x+1, i):
                multiples.append(j)
    return results


