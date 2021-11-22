import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditGlissadeComponent } from './edit-glissade.component';

describe('EditGlissadeComponent', () => {
  let component: EditGlissadeComponent;
  let fixture: ComponentFixture<EditGlissadeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditGlissadeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditGlissadeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
