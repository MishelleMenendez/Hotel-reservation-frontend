import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Reservation {
  id: number;
  check_in: string;
  check_out: string;
  status: string;
  room_id: number;
  created_at: string;
}

@Injectable({
  providedIn: 'root'
})
export class ReservationService {
  private baseUrl = 'http://localhost:5000/reservations';

  constructor(private http: HttpClient) {}

  getUserReservations(userId: number): Observable<Reservation[]> {
    return this.http.get<Reservation[]>(`${this.baseUrl}/?user_id=${userId}`);
  }

  createReservation(userId: number, roomId: number, checkIn: string, checkOut: string): Observable<any> {
    return this.http.post(this.baseUrl + '/', { user_id: userId, room_id: roomId, check_in: checkIn, check_out: checkOut });
  }

  updateReservation(reservationId: number, updates: any): Observable<any> {
    return this.http.put(`${this.baseUrl}/${reservationId}`, updates);
  }

  cancelReservation(reservationId: number): Observable<any> {
    return this.http.delete(`${this.baseUrl}/${reservationId}`);
  }

  getReservationDetails(reservationId: number): Observable<Reservation> {
    return this.http.get<Reservation>(`${this.baseUrl}/${reservationId}`);
  }
}
