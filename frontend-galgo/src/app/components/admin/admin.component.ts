import { Component, inject } from '@angular/core';
import { User } from '../../../models/User';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-admin',
  standalone: false,
  templateUrl: './admin.component.html',
  styles: ``
})
export class AdminComponent {
  private authService = inject(AuthService)
  public user!: User;

  public sidebarItems = [
    { label: 'Inicio', icon: 'home', url: './' },
    { label: 'Categorias', icon: 'category', url: './business/restaurants-types' },
  ]


  logout() {
    this.authService.logout()
  }


}
