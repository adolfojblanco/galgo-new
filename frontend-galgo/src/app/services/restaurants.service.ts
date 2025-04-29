import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { Observable } from 'rxjs';
import { Restaurant } from '../../models/Restaurant';

@Injectable({
  providedIn: 'root'
})
export class RestaurantsService {
  private readonly urlEndPoint: string = `${environment.apiUrl}`;
  private http = inject(HttpClient);

  constructor() { }

  getAllRestaurants(): Observable<Restaurant[]> {
    return this.http.get<Restaurant[]>(`${this.urlEndPoint}/restaurants`);
  }
}
