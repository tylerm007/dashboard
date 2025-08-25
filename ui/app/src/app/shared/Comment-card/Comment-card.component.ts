import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Comment-card.component.html',
  styleUrls: ['./Comment-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Comment-card]': 'true'
  }
})

export class CommentCardComponent {


}