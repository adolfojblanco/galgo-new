import { Component, inject, OnInit } from '@angular/core';
import { RestaurantsService } from '../../../services/restaurants.service';

@Component({
  selector: 'app-restaurants',
  standalone: false,
  templateUrl: './restaurants.component.html',
  styles: ``
})
export class RestaurantsComponent implements OnInit {
  private restService = inject(RestaurantsService)



  ngOnInit(): void {
    this.restService.getAllRestaurants().subscribe((res) => { console.log(res); })
  }



}
