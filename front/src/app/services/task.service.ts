import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
export interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  created_at: string;
}
@Injectable({
  providedIn: 'root'
})
export class TaskService {
  private apiUrl = 'http://127.0.0.1:8000/tasks';
  constructor(private http: HttpClient) {}
  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(this.apiUrl);
  }
  addTask(task: Task): Observable<Task> {
    return this.http.post<Task>(this.apiUrl, task);
  }
  updateTask(taskId: number, taskUpdate: Partial<Task>): Observable<Task> {
    return this.http.put<Task>(`${this.apiUrl}/${taskId}`, taskUpdate);
  }
  deleteTask(taskId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${taskId}`);
  }
}
