import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

// Componentes
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { ResetPasswordComponent } from './components/reset-password/reset-password.component';
import { ProfileComponent } from './components/profile/profile.component';
import { HotelSearchComponent } from './components/hotel-search/hotel-search.component';
import { HotelDetailComponent } from './components/hotel-detail/hotel-detail.component';
import { ReservationListComponent } from './components/reservation-list/reservation-list.component';
import { ReservationFormComponent } from './components/reservation-form/reservation-form.component';
import { ReservationDetailComponent } from './components/reservation-detail/reservation-detail.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { FooterComponent } from './components/footer/footer.component';
import { ErrorComponent } from './components/error/error.component';
import { LoadingSpinnerComponent } from './components/loading-spinner/loading-spinner.component';

// Servicios
import { AuthService } from './services/auth.service';
import { UserService } from './services/user.service';
import { HotelService } from './services/hotel.service';
import { ReservationService } from './services/reservation.service';

// Enrutamiento (agrega tu archivo routing.module.ts si lo tienes)
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    LoginComponent,
    RegisterComponent,
    ResetPasswordComponent,
    ProfileComponent,
    HotelSearchComponent,
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
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AppRoutingModule // si tienes rutas
  ],
  providers: [
    AuthService,
    UserService,
    HotelService,
    ReservationService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
