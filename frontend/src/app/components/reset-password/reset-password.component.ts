import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-reset-password',
  templateUrl: './reset-password.component.html',
  styleUrls: ['./reset-password.component.css']
})
export class ResetPasswordComponent {
  email = '';
  newPassword = '';
  message = '';
  error = false;

  constructor(private authService: AuthService) {}

  onSubmit() {
    this.message = '';
    this.error = false;
    this.authService.resetPassword(this.email, this.newPassword).subscribe({
      next: () => {
        this.message = 'Contraseña restablecida correctamente.';
      },
      error: () => {
        this.error = true;
        this.message = 'Error al restablecer contraseña.';
      }
    });
  }
}
