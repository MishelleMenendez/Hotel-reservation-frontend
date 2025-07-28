import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  user: any;

  constructor(private authService: AuthService) {}

  ngOnInit() {
    const userId = localStorage.getItem('userId');
    if (userId) {
      this.authService.getUserProfile(+userId).subscribe({
        next: (data) => this.user = data,
        error: () => this.user = null
      });
    }
  }
}
