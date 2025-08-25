import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Plant-card.component.html',
  styleUrls: ['./Plant-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Plant-card]': 'true'
  }
})

export class PlantCardComponent {


}