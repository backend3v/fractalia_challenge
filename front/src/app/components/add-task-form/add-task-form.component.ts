import { Component } from '@angular/core';
import { TaskService, Task } from '../../services/task.service';
@Component({
  selector: 'app-add-task-form',
  templateUrl: './add-task-form.component.html',
  styleUrls: ['./add-task-form.component.css']
})
export class AddTaskFormComponent {
  title: string = '';
  description: string = '';
  constructor(private taskService: TaskService) {}
  addTask() {
    const newTask: Task = {
      id: 0,
      title: this.title,
      description: this.description,
      completed: false,
      created_at: new Date().toISOString()
    };
    this.taskService.addTask(newTask).subscribe(() => {
      this.title = '';
      this.description = '';
    });
  }
}
