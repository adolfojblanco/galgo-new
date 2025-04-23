import { inject, Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { jwtDecode } from "jwt-decode";
import { HotToastService } from '@ngxpert/hot-toast';
import { User } from '../../models/User';
import { Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private readonly urlEndPoint: string = `${environment.loginUrl}`;
  private router = inject(Router);
  private http = inject(HttpClient);

  constructor() { }


  login(user: User): Observable<User> {
    return this.http.post<User>(`${this.urlEndPoint}/token/`, user).pipe(
      tap((res: any) => {
        localStorage.setItem('token', res.access);
        this.router.navigate(['/admin']);
      })
    );
  }

  logout(): void {
    localStorage.clear();
    this.router.navigate(['/auth/login']);
  }


  getToken(): string | null {
    const token = localStorage.getItem('token') || null;
    if (token !== null || token !== '') {
      return token;
    }
    return null;
  }

  getAuthUser(): User {
    const token = this.getToken();
    const decoded: User = jwtDecode(token!);
    return decoded;
  }

}
