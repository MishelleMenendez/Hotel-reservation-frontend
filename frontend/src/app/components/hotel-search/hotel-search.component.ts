import { Component } from '@angular/core';
import { HotelService } from '../../services/hotel.service';

@Component({
  selector: 'app-hotel-search',
  templateUrl: './hotel-search.component.html',
  styleUrls: ['./hotel-search.component.css']
})
export class HotelSearchComponent {
  location = '';
  startDate = '';
  endDate = '';
  hotels: any[] = [];
  searched = false;

  constructor(private hotelService: HotelService) {}

  searchHotels() {
    this.hotelService.searchHotels(this.location, this.startDate, this.endDate).subscribe({
      next: (data) => {
        this.hotels = data;
        this.searched = true;
      },
      error: () => {
        this.hotels = [];
        this.searched = true;
      }
    });
  }

  selectHotel(hotel: any) {
    // Puedes emitir evento o navegar a detalle
  }
}
