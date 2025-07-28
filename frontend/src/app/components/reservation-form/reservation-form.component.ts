import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HotelService } from '../../services/hotel.service';
import { ReservationService } from '../..//services/reservation.service';

@Component({
  selector: 'app-reservation-form',
  templateUrl: './reservation-form.component.html',
  styleUrls: ['./reservation-form.component.css']
})
export class ReservationFormComponent implements OnInit {
  reservationForm!: FormGroup;
  hotels: any[] = [];
  rooms: any[] = [];

  constructor(
    private fb: FormBuilder,
    private hotelService: HotelService,
    private reservationService: ReservationService
  ) {}

  ngOnInit(): void {
    this.reservationForm = this.fb.group({
      check_in: ['', Validators.required],
      check_out: ['', Validators.required],
      hotel_id: ['', Validators.required],
      room_id: ['', Validators.required]
    });

    this.hotelService.getHotels().subscribe(data => {
      this.hotels = data;
    });
  }

  onHotelChange(hotelId: string): void {
    this.hotelService.getHotelRooms(hotelId).subscribe(data => {
      this.rooms = data;
    });
  }

  submitReservation(): void {
    if (this.reservationForm.valid) {
      this.reservationService.createReservation(this.reservationForm.value).subscribe();
    }
  }
}
