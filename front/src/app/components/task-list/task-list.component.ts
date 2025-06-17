import { Component, OnInit } from '@angular/core';
import { TaskService, Task } from '../../services/task.service';


@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})



export class TaskListComponent implements OnInit {
  tasks: Task[] = [];
  editTask: Task | null = null;
  constructor(private taskService: TaskService) {}
  ngOnInit(): void {
    this.loadTasks();
  }
  loadTasks() {
    this.taskService.getTasks().subscribe(tasks => {
      this.tasks = tasks;
    });
  }
  toggleTaskCompletion(task: Task) {
  const updatedTask = {
    completed: !task.completed
  };
  this.taskService.updateTask(task.id, updatedTask).subscribe(() => {
    task.completed = !task.completed;
  });
}
  deleteTask(taskId: number) {
    this.taskService.deleteTask(taskId).subscribe(() => {
      this.loadTasks();
    });
  }
  startEdit(task: Task) {
    this.editTask = { ...task };
  }
  saveEdit() {
    if (this.editTask) {
        const updatedTask = {
          title: this.editTask.title,
          description: this.editTask.description,
          completed: this.editTask.completed
        };
        this.taskService.updateTask(this.editTask.id, updatedTask).subscribe(() => {
          this.loadTasks();
          this.editTask = null;
        });
      }
  }
}
