import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReservationService {
  private apiUrl = 'http://localhost:5000/api/reservations';

  constructor(private http: HttpClient) {}

  getMyReservations(): Observable<any[]> {
    const userId = localStorage.getItem('userId');
    return this.http.get<any[]>(`${this.apiUrl}/user/${userId}`);
  }

  getReservationById(id: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/${id}`);
  }

  createReservation(reservationData: any): Observable<any> {
    const userId = localStorage.getItem('userId');
    return this.http.post(`${this.apiUrl}/user/${userId}`, reservationData);
  }
}
