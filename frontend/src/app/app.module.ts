import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { RestPasswordComponent } from './components/rest-password/rest-password.component';
import { ProfileComponent } from './components/profile/profile.component';
import { HotelSearchComponent } from './components/hotel-search/hotel-search.component';
import { ResetPasswordComponent } from './components/reset-password/reset-password.component';
import { HotelDetailComponent } from './components/hotel-detail/hotel-detail.component';
import { ReservationListComponent } from './components/reservation-list/reservation-list.component';
import { ReservationFormComponent } from './components/reservation-form/reservation-form.component';
import { ReservationDetailComponent } from './components/reservation-detail/reservation-detail.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FooterComponent } from './components/footer/footer.component';
import { ErrorComponent } from './components/error/error.component';
import { LoadingSpinnerComponent } from './components/loading-spinner/loading-spinner.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    RestPasswordComponent,
    ProfileComponent,
    HotelSearchComponent,
    ResetPasswordComponent,
    HotelDetailComponent,
    ReservationListComponent,
    ReservationFormComponent,
    ReservationDetailComponent,
    NavbarComponent,
    FooterComponent,
    ErrorComponent,
    LoadingSpinnerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
