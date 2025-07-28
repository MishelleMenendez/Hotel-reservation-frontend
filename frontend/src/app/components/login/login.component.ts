import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html'
})
export class LoginComponent {
  email: string = '';
  password: string = '';
  errorMessage: string = '';

  constructor(private authService: AuthService, private router: Router) {}

  onSubmit(): void {
    this.authService.login(this.email, this.password).subscribe({
      next: (res) => {
        // Aquí podrías guardar un token, por ejemplo:
        // localStorage.setItem('token', res.token);

        // Redirigir al home o dashboard
        this.router.navigate(['/']);
      },
      error: (err) => {
        this.errorMessage = 'Credenciales inválidas. Por favor intenta de nuevo.';
      }
    });
  }
}
