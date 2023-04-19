<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <title>Todo List</title>

        <!-- Fonts -->
        <link href="https://fonts.bunny.net/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">

        <!-- Styles -->
        
        <link rel="stylesheet" href="{{ asset('css/main.css') }}">
        
    </head>
    <body class="antialiased">
            <div class="mainContainer">
                <div class="todoContainer">
                    <p>tasks that need to be done!</p>
                    @foreach(\App\Models\Todo::all() as $task)
                        @if ($task->finished == 0)
                            <div class="task">
                                <p>{{$task->task_to_do}}: {{$task->task_description}}</p>
                            </div>
                        @endif
                    @endforeach
                </div>
                <div class="finishedContainer">
                    <p>finished tasks</p>
                    @foreach(\App\Models\Todo::all() as $task)
                        @if ($task->finished == 1)
                            <div class="task">
                                <p>{{$task->task_to_do}}: {{$task->task_description}}</p>
                            </div>
                        @endif
                    @endforeach
                </div>
            </div>
    </body>
</html>
