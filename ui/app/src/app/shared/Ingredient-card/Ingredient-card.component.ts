import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Ingredient-card.component.html',
  styleUrls: ['./Ingredient-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Ingredient-card]': 'true'
  }
})

export class IngredientCardComponent {


}