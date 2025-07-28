import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Hotel {
  id: number;
  name: string;
  location: string;
  description?: string;
  rating?: number;
  available_rooms?: Room[];
  rooms?: Room[];
}

export interface Room {
  id: number;
  number: string;
  type: string;
  price: number;
  available?: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class HotelService {
  private baseUrl = 'http://localhost:5000/hotels';

  constructor(private http: HttpClient) {}

  searchHotels(location: string, startDate?: string, endDate?: string): Observable<Hotel[]> {
    let params = new HttpParams().set('location', location);
    if (startDate) params = params.set('start_date', startDate);
    if (endDate) params = params.set('end_date', endDate);
    return this.http.get<Hotel[]>(`${this.baseUrl}/search`, { params });
  }

  getHotelDetails(hotelId: number): Observable<Hotel> {
    return this.http.get<Hotel>(`${this.baseUrl}/${hotelId}`);
  }
}
