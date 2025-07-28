import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'] 
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit(): void {
    this.errorMessage = '';

    this.authService.login(this.email, this.password).subscribe({
      next: (response) => {

        localStorage.setItem('userId', response.user_id);
        localStorage.setItem('role', response.role);

        this.router.navigate(['/']);
      },
      error: (err) => {
        this.errorMessage = 'Credenciales inválidas. Por favor intenta de nuevo.';
      }
    });
  }
}
