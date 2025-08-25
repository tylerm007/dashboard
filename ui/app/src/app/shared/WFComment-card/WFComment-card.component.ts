import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './WFComment-card.component.html',
  styleUrls: ['./WFComment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.WFComment-card]': 'true'
  }
})

export class WFCommentCardComponent {


}