import { Component, inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../../services/auth.service';
import { HotToastService } from '@ngxpert/hot-toast';
import { User } from '../../../../models/User';

@Component({
  selector: 'app-login',
  standalone: false,
  templateUrl: './login.component.html',
  styles: [
    `
    .login {
      padding-top: 30px;
    }
    .logo {
      width: 350px;
    }
  `,
  ]
})
export class LoginComponent {
  private authService = inject(AuthService);
  private fb = inject(FormBuilder);
  private toast = inject(HotToastService);
 


  public loginForm: FormGroup = this.fb.group({
    username: ['', [Validators.required]],
    password: ['', [Validators.required]],
  });

  login() {
    this.authService.login(this.loginForm.value).subscribe((res: any) => {
      this.toast.success(`Hola, ${this.authService.getAuthUser().username}`)
    })
  }




}
