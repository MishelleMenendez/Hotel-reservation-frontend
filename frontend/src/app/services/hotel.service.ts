import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HotelService {
  private apiUrl = 'http://localhost:5000/api/hotels';

  constructor(private http: HttpClient) {}

  getHotels(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}`);
  }

  getHotelDetails(hotelId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/${hotelId}`);
  }

  getHotelRooms(hotelId: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/${hotelId}/rooms`);
  }

  searchHotels(location: string, startDate: string, endDate: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/search`, {
      params: { location, start_date: startDate, end_date: endDate }
    });
  }
}
