import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Message-card.component.html',
  styleUrls: ['./Message-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Message-card]': 'true'
  }
})

export class MessageCardComponent {


}