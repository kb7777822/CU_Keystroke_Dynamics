from django.shortcuts import render, redirect, reverse
from snake.models import *
from django.http import HttpResponse, Http404, HttpResponseForbidden
import json

#need to make sure these are the same as in animation.html!! see if they can be shared
bwidth = 500
rsquares = 9
spacing = 5



def animation(request):

    return render(request, 'snake/animation.html')

def getSnakes(request):
    print('getting snakes')
    response_data = []
    if request.method == 'GET':
        for snake in SnakeItem.objects.all():
            my_snake = {
                'color': snake.color,
                'squares': snake.squares
            }
            print(len(SnakeItem.objects.all()))
            print('squares ' + str(snake.squares[0]) + ' color ' + snake.color)
            response_data.append(my_snake)
        response_json = json.dumps(response_data)
        response = HttpResponse(response_json, content_type='application/json')
        return response
    if not 'key' in request.POST or not request.POST['key']:
        #also change this to just keep moving forward
        return _my_json_error_response("You must enter an item to add.")

    key = request.POST['key']
    #OBVIOUSLY CHANGE THIS WHEN THERE'S >1 SNAKE
    for snake in SnakeItem.objects.all():
        if snake.direction == 'N':
            if key == 'd':
                snake = goEast(snake)
            elif key == 'a':
                snake = goWest(snake)
            else: #w,s,or any other key
                snake = goNorth(snake)

        elif snake.direction == 'S':
            if key == 'd':
                snake = goEast(snake)
            elif key == 'a':
                snake = goWest(snake)
            else: #w,s,or any other key
                snake = goSouth(snake)

        elif snake.direction == 'W':
            if key == 'w':
                snake = goNorth(snake)
            elif key == 's':
                snake = goSouth(snake)
            else: #a,d, or any other key
                snake = goWest(snake)
        elif snake.direction == 'E':
            if key == 'w':
                snake = goNorth(snake)
            elif key == 's':
                snake = goSouth(snake)
            else:  # a,d, or any other key
                snake = goEast(snake)
        else:
            _my_json_error_response("invalid snake direction oh no", 404)

        #why are the docs not clear about this????
        tailsquare = snake.squares[0]
        snake.squares.remove(tailsquare)
        snake.save()

        my_snake = {
            'color': snake.color,
            'squares': snake.squares
        }
        response_data.append(my_snake)

    response_json = json.dumps(response_data)
    response = HttpResponse(response_json, content_type='application/json')
    return response


#obviously all these functions will need to check if a snake hits another snake/food
#oh and the snake cant hit itself!! but we'll add that soon

def goNorth(snake):
    headsquare = snake.squares[len(snake.squares)-1]
    if headsquare < rsquares:
        snake = killSnake(snake)
    else:
        snake.squares.append(headsquare-rsquares)
        snake.direction = 'N'
    return snake

def goSouth(snake):
    headsquare = snake.squares[len(snake.squares) - 1]
    if headsquare >= (rsquares*rsquares) - rsquares:
        snake = killSnake(snake)
    else:
        snake.squares.append(headsquare+rsquares)
        snake.direction = 'S'
    return snake

def goWest(snake):
    headsquare = snake.squares[len(snake.squares) - 1]
    if headsquare % rsquares == 0:
        snake = killSnake(snake)
    else:
        snake.squares.append(headsquare-1)
        snake.direction = 'W'
    return snake

def goEast(snake):
    headsquare = snake.squares[len(snake.squares) - 1]
    if headsquare % rsquares == rsquares - 1:
        snake = killSnake(snake)
    else:
        snake.squares.append(headsquare+1)
        snake.direction = 'E'
    return snake

def killSnake(snake):
    print("killed snake")
    snake.squares = [-1, -1]
    return snake

def createSnakes(request):
    #obv obvs we will change this..... each snake starts in the four corners
    new_snake = SnakeItem(color='rgb(255,0,0)',squares=[0],direction='E')
    new_snake.save()
    print("created red snake")
    return getSnakes(request)


def turn(request):

    return render(request, 'snake/animation.html')




def _my_json_error_response(message, status=200):
    # You can create your JSON by constructing the string representation yourself (or just use json.dumps)
    response_json = '{ "error": "' + message + '" }'
    return HttpResponse(response_json, content_type='application/json', status=status)
