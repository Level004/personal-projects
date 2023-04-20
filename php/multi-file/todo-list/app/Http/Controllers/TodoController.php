<?php

namespace App\Http\Controllers;

use App\Models\Todo;
use Illuminate\Http\Request;

class TodoController extends Controller
{
    public function create(Request $request) {
        Todo::create([
            'task_to_do' => $request->taskName,
            'task_description' => $request->taskDescription,
            'finished' => 0,
        ]);

        return redirect()->back()->with('message', 'task added');
    }

    public function delete(Request $request)
    {
        $task = Todo::find($request->taskID);
        $task->delete();

        return redirect()->back()->with('message', 'task deleted');
    }

    public function update(Request $request)
    {
        $task = Todo::find($request->taskID);
        $task->finished = 1;
        $task->update();

        return redirect()->back()->with('message', 'task updated');
    }
}
