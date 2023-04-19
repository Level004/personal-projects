<?php

namespace App\Http\Controllers;

use App\Models\Todo;
use Illuminate\Http\Request;

class TodoController extends Controller
{
    public function update(Request $request)
    {
        $task = Todo::find($request->taskID);
        $task->finshed = 1;
        $task->update();

        return redirect()->back()->with('message', 'task updated');
    }
}
