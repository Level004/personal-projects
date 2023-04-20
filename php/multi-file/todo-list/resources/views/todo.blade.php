<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="csrf-token" content="{{ csrf_token() }}">

        <title>Todo List</title>

        <!-- Fonts -->
        <link href="https://fonts.bunny.net/css2?family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">

        <!-- Styles -->

        <link rel="stylesheet" href="{{ asset('css/main.css') }}">

    </head>
    <body class="antialiased">
            <div class="mainContainer">
                <div class="createTaskContainer">
                    <form method="post" action="todo/create">
                        <label for="taskName">
                            Task Name:
                            <input type="text" name="taskName">
                        </label>
                        <label for="taskDescription">
                            Task Description:
                            <input type="text" name="taskDescription">
                        </label>
                        <button type="submit">
                            add
                        </button>
                    </form>
                </div>
                <div class="todoContainer">
                    <p>tasks that need to be done!</p>
                    @foreach(\App\Models\Todo::all() as $task)
                        @if ($task->finished == 0)
                            <div class="task">
                                <p>{{$task->task_to_do}}: {{$task->task_description}}</p>
                                <form method="post" action="todo/update">
                                    <input type="hidden" name="taskID" value={{$task->id}}>
                                        <button type="submit">
                                            finished!
                                        </button>
                                </form>
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
