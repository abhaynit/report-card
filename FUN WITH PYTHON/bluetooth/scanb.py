from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response('aman kumar')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('192.168.43.17', 8000, application)