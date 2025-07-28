import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ReservationService } from 'src/app/services/reservation.service';

@Component({
  selector: 'app-reservation-detail',
  templateUrl: './reservation-detail.component.html',
  styleUrls: ['./reservation-detail.component.css']
})
export class ReservationDetailComponent implements OnInit {
  reservation: any;
  loading = true;
  error = false;

  constructor(
    private route: ActivatedRoute,
    private reservationService: ReservationService,
    private router: Router
  ) {}

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      this.reservationService.getReservationById(id).subscribe({
        next: data => {
          this.reservation = data;
          this.loading = false;
        },
        error: err => {
          console.error('Error cargando reserva', err);
          this.loading = false;
          this.error = true;
        }
      });
    }
  }

  volver(): void {
    this.router.navigate(['/reservations']);
  }
}
