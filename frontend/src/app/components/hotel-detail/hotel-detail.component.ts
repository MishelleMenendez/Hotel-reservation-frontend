import { Component, Input, OnChanges } from '@angular/core';
import { HotelService } from '../../services/hotel.service';

@Component({
  selector: 'app-hotel-detail',
  templateUrl: './hotel-detail.component.html',
  styleUrls: ['./hotel-detail.component.css']
})
export class HotelDetailComponent implements OnChanges {
  @Input() hotelId: number | null = null;
  hotel: any = null;

  constructor(private hotelService: HotelService) {}

  ngOnChanges() {
    if (this.hotelId) {
      this.hotelService.getHotelDetails(this.hotelId).subscribe({
        next: (data) => this.hotel = data,
        error: () => this.hotel = null
      });
    }
  }
}
